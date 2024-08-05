# Pastefo collector


The [main.py](https://github.com/kaykRodr1gu3s/data-leak-monitoring/blob/main/Pastefo/main.py) script is designed to systematically collect and analyze user data from the recent posts on [Pastefo](https://paste.fo/recent). This script performs the following key functions:

 1. Collect User Links: It navigates to the recent posts page on Pastefo and extracts all available user links.
 2. Retrieve User Information: For each user link gathered, the script fetches detailed information about the user, including:

    + Contact Details: Any available contact information provided by the user.
    + Number of Pastes: The total number of pastes the user has created.
    + Number of Views: The total number of views across all pastes created by the user.
    + Paste Content: The actual content of each paste made by the user.

    Data Storage: All the collected information is saved in a structured JSON format, facilitating easy access and further analysis.

This automation ensures efficient data collection and organization, making it easier to monitor and analyze user activity on Pastefo.

Additionally, I will upload the collected data to Splunk using the Splunk SDK.
