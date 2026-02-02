# dtsc330

# HW 2

How do you fill in the missing dates from the grants data?
    - Made loop to look at range of missing dates
        ○ Rows 65925-70459
    - Trouble finding pattern
        ○ Out of order
    - Decided to use the average date for NaNs
        ○ Looked for last dates entered between NaNs and filled in midpoint date

PI_NAMEs contains multiple names. We can only connect individual people. Can you make it so that we can get "grantees"?
Split PI_NAMES into different rows using pandas
    - Clean pi names
        ○ Remove (contact)
        ○ Get rid of whitespace
        ○ Determine delimiters
    - Split pi names into list of individual names
        ○ Used explode() to create one row per investigator
    - Removed empty/missing entries and retained application ID between each person and their grant
    - Create normalized grantees table with one person per row

The dates for Articles are problematic. Can you fix them?
    - Look at how dates are formatted
    - Determine what tag we're parsing
        ○ PubDate vs. others
    - If PubDate tag: extra loop
        ○ If tags are month, day, year: save into variable
Format into year-month-day