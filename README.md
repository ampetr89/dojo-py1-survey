# My first Flask app!

The landing page has a form, which upon submission redirects you to the results page. The data you enter in the form is sent via a POST request, and used to populate the results page. The results page uses [Jinga](jinja.pocoo.org) to render the result page template and inject the data values received from the form. 