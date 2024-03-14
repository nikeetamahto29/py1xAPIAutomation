from source.constants.api_constants import BASE_URL ,APIconstants


def test_crud():
  print(BASE_URL)

 # url_direc_func = base_url()
 # print(url_direc_func)

  url_class = APIconstants.base_url()
  print(url_class)