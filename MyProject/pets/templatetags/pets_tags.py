from django import template

register = template.Library()

@register.simple_tag
def filter_url(val, f_name, url_encode=None):
    url ='?{}={}'.format(f_name, val)
    
    if url_encode:
        query = url_encode.split('&')
        query_filtered = filter(lambda p: p.split('=')[0]!=f_name, query)
        query_encoded = '&'.join(query_filtered)
        url = '{}&{}'.format(url, query_encoded)
    return url

# final url : ?page=1&pet_type=Gryzoń&gender=Samica&region=Dolnośląskie
# url = ?page=1
# query = page=2&pet_type=&gender=Saminca&region=Dolnośląskie
# query_filtered = ['pet_type=', 'gender=', 'region=']
# query_encoded = pet_type=&gender=Saminca&region=Dolnośląskie
# url = {?page=1}{pet_type=&,gender=Saminca&region=Dolnośląskie}

#         print(f"Main  url:{url}")
#         print(f"Query string:{query}")
#         print(f"Filtered Query string:{query_filtered}")
#         print(f"Encoded Query string:{query_encoded}")
#         print(f"Final url :{url}")