# Python - Network #0

Welcome to the Python Networking Project! In this project, I utilized the power of `curl` in Bash scripts to facilitate the exchange of various types of HTTP headers. As a result of this exploration, I gained insights into the intricate workings of URLs, domain names, the diverse array of HTTP request and response header fields, status codes, and even the art of handling cookies.

## Learning Highlights :rocket:

Throughout the project, I delved into a series of tasks that not only honed my networking skills but also expanded my programming horizon. Additionally, Task Six introduced an intriguing algorithmic challenge in Python, providing an exciting departure from the project's main theme.

## Project Tasks :page_with_curl:

Please note that all Bash scripts leveraging `curl` were meticulously crafted to interact seamlessly with a server configured within a container.

* **Task 0: cURL Body Size**
  [0-body_size.sh](./0-body_size.sh): A Bash script that dispatches a `GET` request to a specified URL and accurately presents the size of the response body in bytes.

* **Task 1: cURL to the End**
  * [1-body.sh](./1-body.sh): This Bash script orchestrates a `GET` request to a designated URL and elegantly displays the response body, exclusively for responses with a `200` status code.

* **Task 2: cURL Method**
  * [2-delete.sh](./2-delete.sh): Delving into the DELETE realm, this Bash script gracefully sends a `DELETE` request to a given URL and presents the resulting response body.

* **Task 3: cURL Only Methods**
  * [3-methods.sh](./3-methods.sh): Curious about the server's accepted HTTP methods? This Bash script ingeniously reveals all HTTP methods the server of a designated URL is willing to accommodate.

* **Task 4: cURL Headers**
  * [4-header.sh](./4-header.sh): With a flair for headers, this Bash script conducts a `GET` request to a specific URL, adorned with the `X-HolbertonSchool-User-Id=98` header, and elegantly presents the response body.

* **Task 5: cURL POST Parameters**
  * [5-post_params.sh](./5-post_params.sh): Behold the power of POST! This Bash script orchestrates a `POST` request to a chosen URL, equipped with the variables `email=test.gmail.com` and `subject=I will always be here for PLD`, and gracefully unveils the response body.

* **Task 6: Find a Peak**
  * [6-peak.py](./6-peak.py): Embarking on a [Technical Interview Preparation] adventure, this Python program deftly identifies a peak within an unsorted list of integers.
  * [6-peak.txt](./6-peak.txt): Peek into this text file to gain insights into the algorithm's complexity.

* **Task 7: Only Status Code**
  * [100-status_code.sh](./100-status_code.sh): A Bash script that ingeniously captures a `GET` request's status code for a given URL, sans the use of pipes, redirections, `;`, or `&&`.

* **Task 8: cURL a JSON File**
  * [101-post_json.sh](./101-post_json.sh): Unleashing the prowess of JSON, this Bash script orchestrates a JSON-powered `POST` request with the contents of a designated file to a chosen URL and artfully presents the response body.

* **Task 9: Catch Me if You Can!**
  * [102-catch_me.sh](./102-catch_me.sh): Prepare for a whimsical journey as this Bash script sends a request to `0.0.0.0:5000/catch_me`, triggering a server response that playfully exclaims `You got me!`.

Feel free to explore, learn, and embrace the diverse challenges and discoveries that await in this networking and Python-powered adventure!
