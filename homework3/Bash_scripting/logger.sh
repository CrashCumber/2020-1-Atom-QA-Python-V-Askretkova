file='access.log'

if [[ "$1" = '' ]]
then
    path="./$file"
else
    end=`echo "$1" | grep '/$'`
    if [[ "$end" = '/' ]]
    then
      path="$1$file"
    else
      path="$1/$file"
    fi
fi

num_requests=`cat $path | grep ' - - ' | wc -l | tr -s ' ' | cut -f2 -d ' '`
echo -e "$num_requests  \n" > record_bash.sh

num_requests_by_method=`cat $path | cut -f6 -d ' ' | sort | uniq -c | tr -d '"'  `
echo -e "$num_requests_by_method  \n" >> record_bash.sh

top_size_requests=`cat $path | sort -k10 -n -r| cut -f1,4,5,6,7,10 -d ' ' | head | tr -d '"'  `
echo -e "$top_size_requests   \n" >> record_bash.sh

top_requests_client_error=`cat $path | awk '$9 ~ /^4/ {print $1, $6, $7, $9 }' | sort  | uniq -c| sort -r -n | head | tr -d '"' `
echo -e "$top_requests_client_error  \n" >> record_bash.sh

top_requests_redirect=`cat $path | awk '$9 ~ /^3/ {print $1, $6, $7, $9 }' | sort  | uniq -c| sort -r -n | head | tr -d '"' `
echo -e "$top_requests_redirect  \n" >> record_bash.sh



