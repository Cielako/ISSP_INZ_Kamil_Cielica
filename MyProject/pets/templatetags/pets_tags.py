from django import template

register = template.Library()

@register.simple_tag
def filter_url(value, field_name, urlencode=None):
    url ='?{}={}'.format(field_name, value)
    
    if urlencode:
        querystring = urlencode.split('&')
        filtered_querystring = filter(lambda p: p.split('=')[0]!=field_name, querystring)
        encoded_querystring = '&'.join(filtered_querystring)
        url = '{}&{}'.format(url, encoded_querystring)
    return url

# final url : ?page=1&pet_type=Gryzoń&gender=Samica&region=Dolnośląskie
# url = ?page=1
# querystring = page=2&pet_type=&gender=Saminca&region=Dolnośląskie
# filtered_querystring = ['pet_type=', 'gender=', 'region=']
# encoded_querystring = pet_type=&gender=Saminca&region=Dolnośląskie
# url = {?page=1}{pet_type=&,gender=Saminca&region=Dolnośląskie}

#         print(f"Main  url:{url}")
#         print(f"Query string:{querystring}")
#         print(f"Filtered Query string:{filtered_querystring}")
#         print(f"Encoded Query string:{encoded_querystring}")
#         print(f"Final url :{url}")