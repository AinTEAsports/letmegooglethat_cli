import sys
import clipboard

QUERY_TEMPLATE = r"https://letmegooglethat.com/?q={QUERY}"


if len(sys.argv) == 1:
    sys.exit()

# sys.argv[0] is script name so I don't take it
query_search = '+'.join(sys.argv[1:])
url = QUERY_TEMPLATE.format(QUERY=query_search)

clipboard.copy(url)

