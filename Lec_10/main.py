import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def filter_titles_with_less_than_6_words(data):
    """Filter out titles with more than 6 words."""
    return [item for item in data if len(item["title"].split()) <= 6]


def filter_bodies_with_less_than_3_lines(data):
    """Filter out items where body has more than 3 lines."""
    return [item for item in data if len(item["body"].split("\n")) <= 3]


def get_filtered_data():
    response = requests.get(f"{BASE_URL}/posts")
    if response.status_code == 200:
        data = response.json()
        data = filter_titles_with_less_than_6_words(data)
        data = filter_bodies_with_less_than_3_lines(data)
        return data
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return []


def create_post():
    payload = {
        "title": "New Post",
        "body": "This is a new post for demonstration.",
        "userId": 1,
    }
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    if response.status_code == 201:
        print("Post created successfully:", response.json())
    else:
        print("Failed to create post.")


def update_post(post_id):
    payload = {
        "id": post_id,
        "title": "Updated Title",
        "body": "This is an updated body.",
        "userId": 1,
    }
    response = requests.put(f"{BASE_URL}/posts/{post_id}", json=payload)
    if response.status_code == 200:
        print("Post updated successfully:", response.json())
    else:
        print(f"Failed to update post {post_id}.")


def delete_post(post_id):
    response = requests.delete(f"{BASE_URL}/posts/{post_id}")
    if response.status_code == 200:
        print(f"Post {post_id} deleted successfully.")
    else:
        print(f"Failed to delete post {post_id}.")


if __name__ == "__main__":
    print("GET Request - Filtered Data:")
    filtered_data = get_filtered_data()
    for item in filtered_data[:5]:
        print(item)

    print("\nPOST Request - Creating a Post:")
    create_post()

    print("\nPUT Request - Updating a Post:")
    update_post(1)

    print("\nDELETE Request - Deleting a Post:")
    delete_post(1)