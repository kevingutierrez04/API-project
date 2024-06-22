import requests

def story():
  response =  requests.get("https://hacker-news.firebaseio.com/v0/newstories.json")
  story_ids = response.json()

  most_recent_story_id = story_ids[0]

  story_details_url = f"https://hacker-news.firebaseio.com/v0/item/{most_recent_story_id}.json"
  story_response = requests.get(story_details_url)
  story_details = story_response.json()
story()