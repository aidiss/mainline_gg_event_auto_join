# mainline_gg_event_auto_join

Be sure to login fast!

Requires chromedriver to be in path. Download it from https://chromedriver.storage.googleapis.com/index.html?path=2.38/

`selenium` is required too.
`ipython` and `jupyter` are recommended.

Flow:
1. Open Jupyter notebook
2. Start chrome webdriver.
3. Loging to your account.
4. Go to event page (currently tested only with PUBG)
5. Guess the match id element for the next event (F12 to inspect elements)
6. Enter the id and start the cell that contains the cycle
