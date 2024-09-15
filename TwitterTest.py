import requests
import re
import time

def get_tweets(username, tweet_count=10):
    url = f"https://twitter.com/{username}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/58.0.3029.110 Safari/537.36'}
    
    proxies = {
        "http": "http://ifwpnzcz:95i6otmb3qj9@38.154.227.167:5868"
    }
    
    response = requests.get(url, headers=headers, proxies=proxies)
    
    if response.status_code != 200:
        print(f"Failed to get data from Twitter, status code: {response.status_code}")
        return []
    
    html_content = response.text
    tweet_texts = re.findall(r'data-testid="tweetText.*?>(.*?)<', html_content)
    
    clean_tweets = []
    for tweet in tweet_texts:
        # Clean HTML tags from the tweet text
        clean_text = re.sub(r'<.*?>', '', tweet)
        clean_tweets.append(clean_text)
        
        if len(clean_tweets) == tweet_count:
            break
    
    return clean_tweets

def main():
    username = "elonmusk"
    
    while True:
        try:
            tweets = get_tweets(username)
            for tweet in tweets:
                print(tweet)
            break
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            print("Retrying after a delay...")
            time.sleep(5)  # Delay before retrying

if __name__ == "__main__":
    main()