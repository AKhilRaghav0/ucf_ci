## Udemy Coupon Fetcher

This is a Python script for fetching Udemy coupons from the website [DiscUdemy](https://www.discudemy.com/). The coupons are saved in a text file named "coupons.txt".

### Required Libraries

- [requests](https://pypi.org/project/requests/)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)

### How to Use over local system

1. Clone the repository and navigate to the folder.
2. Install the required libraries using `pip install -r requirements.txt`.
3. Run the script using `python script.py`.
4. Check the "coupons.txt" file in the "ucf" folder in your downloads directory.

### How to Use over Ci/CD workflows

1. Open Actions section
2. Select workflow file
3. Do Workflow Dispatch

After running the workflow, the coupon links and code will be stored in a compressed archive format in the "Artifacts" section of the workflow run. The compressed archive will be in ".zip" format, and can be easily downloaded and extracted to access the "coupons.txt" file containing the coupon links and script.

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=AKhilRaghav0/ucf_ci&type=Date)](https://star-history.com/#AKhilRaghav0/ucf_ci&Date)

------
Note: This script is made for educational purposes only. Any misuse of this tool is not the author's responsibility.
