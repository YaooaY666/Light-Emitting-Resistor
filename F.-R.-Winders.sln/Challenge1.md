## Challenge 1 - The Locked Door

## Step 1: Web Challenge
After clicking the DOOR link, we viewed the page source to find the directory to the access log page by viewing the html code. We found it to be `/dwvdtoub` when looking at the styling for the disabled ‘Access Log’ button. This brings us to the access log page by appending `/dwvdtoub` to the webpage address. 
Viewing page source once again, we found a hint to use SQL injection for the password, since this comment `<! – remember to prevent sql injection – >` was left in the line containing the text input for the password. 
Using SQL injection, we tried several options, such as `“admin’ OR 1=1 –-”` and `“admin’ OR NULL IS NULL -- “`, for which the latter worked. 
Here, the `WHERE` statement in the SQL query evaluates to `true`, as the username matches and even though the password is false, the condition `NULL IS NULL` is always true. We were thus able to download the .pcap file.

## Step 2: Crypto Challenge
