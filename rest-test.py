import requests


def main():

    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    url = "http://chrisgtest.wpengine.com/wp-json/wp/v2/posts/"
    print(requests.get(url))

    # set up the parameters - basic login details from the environment variables
    user = "api" #os.environ['WP_USER']
    password = "UN6vBeC4mj9OG8Ka@IC9xd%c" #os.environ['WP_PASS']
    form_data = {
        'title': "test",
        'body': '<h1>TEST</h1>',
        'status': 'publish'
    }

    # send the data and get the response back
    response = requests.request(
        "POST",
        url,
        data=form_data,
        auth=(user, password))

    if (response.status_code == 403):
        print(response)
        exit()

    # parse the response via the JSON library
    json = response.json()

    return json['guid']['rendered']


if __name__ == "__main__":

        # main loop
        main()


