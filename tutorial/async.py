import aiohttp
import asyncio
import json


async def fetch():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://jsonplaceholder.typicode.com/posts") as response:
            return await response.json()

# Run the async function
async def main():
    data = await fetch()

    target_id = 10  # The ID we're looking for
    
    # Convert filter object to list immediately
    filtered_posts = list(filter(lambda post: post['id'] == target_id, data))
    
    if not filtered_posts:  # Check if list is empty
        print(f"No posts found with id == {target_id}")
    else:
        print(filtered_posts)  # Print the matching post(s)

# Execute the async event loop
asyncio.run(main())