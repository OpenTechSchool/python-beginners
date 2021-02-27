#!/usr/bin/bash
project="python-for-beginners"
pots="_build/locale/en"
pos="source/locale/<lang>/LC_MESSAGES"

for f in $pots/*.pot; do
    r=$(basename $f '.pot')
    echo $f
    echo "$project.$r"
    tx set --auto-local -r "$project.$r" \
        "$pos/$r.po" \
        --source-file "$f" \
        --source-language=en --execute
done
