import pdfkit
import jinja2
from datetime import datetime

today_date = datetime.today().strftime("%d.%m.%Y")
import jinja2
import pdfkit
from datetime import datetime

client_name = "Sami A"

today_date = datetime.today().strftime("%d %b, %Y")
month = datetime.today().strftime("%B")

context = {
           'report_id': '4058216',
           'client_name': client_name, 
           'company_name': 'Electro Volt GmbH',
           'company_address_street': 'Karl-Ebert-Str. 1',
           'company_address_postal_code': '80555',
           'company_address_country': 'Germany',
           'company_email': 'info@electrovolt.de',
           'company_weblink': 'www.electrovolt.de',

           'subject_service': 'Splicer Repairs 4058216', 
           'customer_id': '2410011', 
           'operation_id': '0020', 
           'notification_id': '000300113570', 
           'job_type': 'Field Service', 
           'start_date': '21.02.2023', 
           'end_date': '25.02.2023' 
           }

template_loader = jinja2.FileSystemLoader('./')
template_env = jinja2.Environment(loader=template_loader)

html_template = 'reportTemplate.html'
template = template_env.get_template(html_template)
output_text = template.render(context)

config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')
output_pdf = 'report.pdf'
pdfkit.from_string(output_text, 
                   output_pdf, 
                   configuration=config, 
                   css='reportTemplate.css',
                   options={"enable-local-file-access": ""})