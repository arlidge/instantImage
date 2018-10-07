from src.instantImage import instantImage

if __name__ == '__main__':

    print("Lets find some images")
    keyword = str(input("Enter keyword to search for: "))
    instagram_limit = int(input("How many images would you like per request? "))


    scraper = instantImage()
    scraper.Scrape_Instagram(tag=keyword,
                              limit=instagram_limit,
                              browser='chrome') # 'chrome' or 'firefox'

    print("Stopping instantImage")
