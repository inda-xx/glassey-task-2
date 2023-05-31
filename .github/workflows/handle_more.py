def main():
    title = "🤖 Here's an extra task for you!"
    body = "This is a dummy body"
    print(f"::set-output name=title::{title}")
    print(f"::set-output name=body::{body}")

if __name__ == "__main__":
    main()
 
