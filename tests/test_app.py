from playwright.sync_api import Page, expect


"""
homepage has message and all peeps from latest to oldest
has links to each user in each post
has links to the tagged users in each post
"""
def test_homepage_peeps(db_connection, page, test_web_address):
    db_connection.seed('seeds/chitter_.sql')
    page.goto(f'http://{test_web_address}/')
    expect(page).to_have_title("Chitter")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text(["Welcome to Chitter", "Cheets"])
    p_tag = page.locator("p")
    expect(p_tag).to_have_text(["You are lo"])



"""
home has links to a user page
takes to that page with a list of their peeps
"""

"""
home has a link to the login page
email, password, login button
takes back to homepage
"""

"""
home has a logout button
message saying logged out
peeps still on page
"""

"""
user page has a list of peeps in reverse order
"""