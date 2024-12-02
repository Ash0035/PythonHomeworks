import requests

base_url = "https://jsonplaceholder.typicode.com/posts"


def get_and_filter():
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        filtered_titles = [item for item in data if len(item["title"].split()) <= 6]
        filtered_data = [
            item for item in filtered_titles if len(item["body"].split("\n")) <= 3
        ]
        print("Filtered Data:", filtered_data)
        return filtered_data
    else:
        print(f"GET request failed with status code: {response.status_code}")
        return []


def create_post():
    new_data = {
        "title": "New Post",
        "body": "This is the body of the new post.",
        "userId": 1,
    }
    response = requests.post(base_url, json=new_data)
    if response.status_code == 201:
        print("Post created successfully:", response.json())
        return response.json()
    else:
        print(f"POST request failed with status code: {response.status_code}")


def update_post(post_id):
    if post_id:
        updated_data = {"title": "Updated Post"}
        print(f"Attempting to PATCH post with ID: {post_id}")
        response = requests.patch(f"{base_url}/{post_id}", json=updated_data)
        if response.status_code == 200:
            print("Post updated successfully:", response.json())
            return response.json()
        else:
            print(f"PATCH request failed with status code: {response.status_code}")
            print("Response text:", response.text)
    else:
        print("Invalid post ID provided.")


def delete_post(post_id):
    if post_id:
        response = requests.delete(f"{base_url}/{post_id}")
        if response.status_code == 200:
            print("Post deleted successfully.")
        else:
            print(f"DELETE request failed with status code: {response.status_code}")
    else:
        print("Invalid post ID provided.")


if __name__ == "__main__":
    print("Starting GET request...")
    filtered_data = get_and_filter()

    print("\nStarting POST request...")
    created_post = create_post()

    if created_post:
        print("\nStarting PUT request...")
        update_post(created_post["id"])

    print("\nStarting DELETE request...")
    delete_post(1)