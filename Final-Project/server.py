import http.server
import socketserver
import termcolor
import serverutils as su
from urllib.parse import urlparse, parse_qs
import json
from Seq_class import Seq

# Define the Server's port
PORT = 8081

SERVER = "rest.ensembl.org"
PARAMS = "?content-type=application/json"

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True

DICT_GENES = {
    "FRAT1": "ENSG00000165879",
    "ADA": "ENSG00000196839",
    "FXN": "ENSG00000165060",
    "RNU6_269P": "ENSG00000212379",
    "MIR633": "ENSG00000207552",
    "TTTY4C": "ENSG00000228296",
    "RBMY2YP": "ENSG00000227633",
    "FGFR3": "ENSG00000068078",
    "KDR": "ENSG00000128052",
    "ANK2": "ENSG00000145362"
}

# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""
        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        termcolor.cprint(self.path, 'blue')

        o = urlparse(self.path)
        path_name = o.path
        arguments = parse_qs(o.query)
        print("Resource requested: ", path_name)
        print("Parameters:", arguments)

        context = {}
        connection = http.client.HTTPConnection(SERVER)

        if path_name == '/':
            context['list'] = DICT_GENES.keys()
            contents = su.read_template_html_file('./html/index.html').render(context=context)

        elif path_name == '/listSpecies':
            endpoint = '/info/species'
            connection.request("GET", endpoint + PARAMS)
            response = connection.getresponse()
            response_dict = json.loads(response.read().decode())
            lista = []
            try:
                limit = arguments['limit'][0]
                if limit.isdigit():
                    for spec in (response_dict['species'][0:int(limit)]):
                        lista.append(spec['name'])
                    context['limit'] = limit
                    context['list'] = lista
                    context['length'] = len(response_dict['species'])
                    contents = su.read_template_html_file('./html/get_list.html').render(context=context)
                else:
                    contents = su.read_template_html_file('./html/ERROR.html').render()
            except KeyError:
                contents = su.read_template_html_file('./html/ERROR.html').render()

        elif path_name == '/karyotype':
            endpoint = '/info/assembly/'
            try:
                species = arguments['species'][0]
                connection.request("GET", endpoint + species + PARAMS)
                response = connection.getresponse()
                response_dict = json.loads(response.read().decode())
                lista = []
                try:
                    for chromo in (response_dict['karyotype']):
                        lista.append(chromo)
                    context['list'] = lista
                    contents = su.read_template_html_file('./html/karyotype.html').render(context=context)
                except KeyError:
                    contents = su.read_template_html_file('./html/ERROR.html').render()
            except KeyError:
                contents = su.read_template_html_file('./html/ERROR.html').render()

        elif path_name == '/chromosomeLength':
            endpoint = '/info/assembly/'
            try:
                species = arguments['species'][0]
                connection.request("GET", endpoint + species + PARAMS)
                response = connection.getresponse()
                response_dict = json.loads(response.read().decode())
                chromo = arguments['chromo'][0]
                for dictionary in response_dict['top_level_region']:
                    if dictionary['name'] == chromo:
                        context['chromo'] = chromo
                        context['length'] = dictionary['length']
                        contents = su.read_template_html_file('./html/chromo_len.html').render(context=context)
                        break
                    else:
                        pass
                    contents = su.read_template_html_file('./html/ERROR.html').render()
            except KeyError:
                contents = su.read_template_html_file('./html/ERROR.html').render()

        elif path_name == '/geneSeq':
            endpoint = '/sequence/id/'
            id = DICT_GENES[arguments['gene'][0]]
            connection.request("GET", endpoint + id + PARAMS)
            response = connection.getresponse()
            response_dict = json.loads(response.read().decode())
            context = {
                'seq': response_dict['seq'],
                'gene': arguments['gene'][0]
            }
            contents = su.read_template_html_file('./html/geneSeq.html').render(context=context)

        elif path_name == '/geneInfo':
            endpoint = '/sequence/id/'
            id = DICT_GENES[arguments['gene'][0]]
            connection.request("GET", endpoint + id + PARAMS)
            response = connection.getresponse()
            response_dict = json.loads(response.read().decode())
            info = response_dict['desc']
            context = {
                'gene': arguments['gene'][0],
                'start': (info.split(':'))[3],
                'end': (info.split(':'))[4],
                'length': (int((info.split(':'))[4]) - int((info.split(':'))[3]) + 1),
                'id': id,
                'chromo_name': (info.split(':'))[2]
            }
            contents = su.read_template_html_file('./html/geneInfo.html').render(context=context)

        elif path_name == '/geneCalc':
            endpoint = '/sequence/id/'
            id = DICT_GENES[arguments['gene'][0]]
            connection.request("GET", endpoint + id + PARAMS)
            response = connection.getresponse()
            response_dict = json.loads(response.read().decode())
            sequence = response_dict['seq']
            length = Seq(sequence).len()
            bases = Seq(sequence).percentage_base(Seq(sequence).count_bases(), length)
            context = {
                'gene': arguments['gene'][0],
                'length': length,
                'bases': bases.items()
            }
            contents = su.read_template_html_file('./html/geneCalc.html').render(context=context)

        else:
            contents = su.read_template_html_file('./html/ERROR.html').render()

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()