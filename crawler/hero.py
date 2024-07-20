import time
import csv
from urllib.request import urlopen
from urllib.request import Request
import json
from urllib.parse import quote_plus


def get_results(search, headers, page, stars):
    # 对搜索关键词进行 URL 编码
    encoded_search = quote_plus(search)
    url = 'https://api.github.com/search/repositories?q={search}%20stars:<={stars}&page={num}&per_page=100&sort=stars' \
          '&order=desc'.format(search=encoded_search, num=page, stars=stars)
    req = Request(url, headers=headers)
    response = urlopen(req).read()
    result = json.loads(response.decode())
    return result


if __name__ == '__main__':
    # Specify the search keyword with AND operator
    search = '"sustech" AND "ee"'

    # Modify the GitHub token value
    headers = {'User-Agent': 'Mozilla/5.0',
               'Authorization': 'token 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',
               'Content-Type': 'application/json',
               'Accept': 'application/json'
               }

    count = 1
    # Set an initial high value for stars
    stars = 421701
    repos_list = []
    
    # Loop through pages of results
    for i in range(0, 2):  # Change the range if you want to fetch more pages
        stars_list = []
        for page in range(1, 11):  # Fetch up to 10 pages
            results = get_results(search, headers, page, stars)
            for item in results['items']:
                repos_list.append([count, item["name"], item["clone_url"], item["stargazers_count"]])
                stars_list.append(item["stargazers_count"])
                count += 1
            print(f"Page {page} processed. Total repositories collected: {len(repos_list)}")
        
        # Update stars to the minimum stars from the last page
        stars = stars_list[-1] if stars_list else stars
        print(f"Next star threshold: {stars}")

        # Save to CSV file
        with open("./sustech_ee_repos.csv", "w", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(['ID', 'Name', 'Clone URL', 'Stars'])
            writer.writerows(repos_list)
        print("Data saved to sustech_ee_repos.csv")

        # For authenticated requests, 30 requests per minute
        # For unauthenticated requests, the rate limit allows you to make up to 10 requests per minute.
        time.sleep(60)
