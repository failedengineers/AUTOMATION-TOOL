import pandas as pd
import re
import time



start_time = time.time()




INPUT_FILE = "hridik.xlsx"#change here

EMAIL_OUTPUT_FILE = "hridik_emails.csv"#change here
LINK_OUTPUT_FILE = "hridik_links.csv"# change here




dataframe = pd.read_excel(INPUT_FILE)





email_regex = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

linkedin_regex = (
    r"https?://lnkd\.in/[A-Za-z0-9_-]+"
)




all_emails = []
all_linkedin_urls = []


for row_content in dataframe["content"].dropna():

    text = str(row_content)

    # Extract emails
    extracted_emails = re.findall(
        email_regex,
        text
    )

    all_emails.extend(extracted_emails)

    # Extract LinkedIn short links
    extracted_links = re.findall(
        linkedin_regex,
        text
    )

    all_linkedin_urls.extend(extracted_links)


unique_emails = sorted(
    list(set(all_emails))
)

unique_linkedin_urls = sorted(
    list(set(all_linkedin_urls))
)


emails_df = pd.DataFrame(
    unique_emails,
    columns=["email"]
)

emails_df.to_csv(
    EMAIL_OUTPUT_FILE,
    index=False
)




linkedin_df = pd.DataFrame(
    unique_linkedin_urls,
    columns=["linkedin_url"]
)

linkedin_df.to_csv(
    LINK_OUTPUT_FILE,
    index=False
)



end_time = time.time()

total_runtime = round(
    end_time - start_time,
    2
)

print(f"\nExtracted {len(unique_emails)} unique emails")
print(f"Extracted {len(unique_linkedin_urls)} LinkedIn URLs")

print(f"\nFiles saved:")
print(f"-> {EMAIL_OUTPUT_FILE}")
print(f"-> {LINK_OUTPUT_FILE}")

print(f"\nCompleted in {total_runtime} seconds")
