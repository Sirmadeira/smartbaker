from django.test import SimpleTestCase
from django.urls import reverse,resolve
from baker.views import home,about
"""

Utilizado para testes sem modelos

"""



class TestUrls(SimpleTestCase):


    """
    test_baker_urls - Função que garante que o pathing que estamos fazendo ate a  nossa view
    é o esperado pelo django, em resumo estamos clicando e verificando se a URL é direcionada view
    
    """
    def test_baker_urls_home(self):
        url = reverse(viewname = 'baker-home')
        print(resolve(path = url))
        self.assertEqual(resolve(url).func, home)

    def test_baker_urls_about(self):
        url = reverse(viewname = 'baker-about')
        print(resolve(path = url))
        self.assertEqual(resolve(url).func, about)