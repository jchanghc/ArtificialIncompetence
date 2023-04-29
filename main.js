const puppeteer = require('puppeteer');
const fs = require('fs');
const handlebars = require('handlebars');

async function generatePDF(htmlFile, cssFile, context) {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();

    //read the html and css files
    const htmlContent = fs.readFileSync(htmlFile, 'utf8');
    const template = handlebars.compile(htmlContent);
    const html = template(context);
    const css = fs.readFileSync(cssFile, 'utf8');
    await page.setContent(html);

    //set page content
    await page.setContent(html);

    await page.addStyleTag({ content: css });

    const pdfBuffer = await page.pdf({format: 'A4'});
    fs.writeFileSync('report.pdf', pdfBuffer)
    await browser.close();
}


context = {
    'report_id': '4058216',
    'client_name': "Jonathan", 
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

generatePDF('reportTemplate.html','reportTemplate.css', context)