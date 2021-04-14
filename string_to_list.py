import sys

def list_from_text(text):
    """
    This function extracts a list of pages separated by commas.
    Hypens indicate a continuous list of pages
    1-5 : 1,2,3,4,5
    1-5,6,9,10-12: 1,2,3,4,5,6,9,10,11,12
    """
  
    range_list = list(text.split(","))
    page_list = []
    for ranges in range_list:
        if "-" in ranges:
            single_range_start_end = list(ranges.split("-"))

            # Check for sanity in each range
            # check if there are only two values
            if(len(single_range_start_end)!=2):
                continue

            # one of the values might be '' or not a number
            try:
                single_range_start_end = list(map(int,single_range_start_end))
            except:
                continue

            start = single_range_start_end[0]
            # because we want the range to be inclusive
            end = single_range_start_end[1]+1 

            # if the range is put from back to front, flip it
            if start > end:
                temp = end-1
                end = start+1
                start = temp
            
            # create the range
            single_range_list = list(range(start,end))

            # add to the current list
            page_list.extend(single_range_list)
        else:
            # if it is just a number/single character
            try:
                page_list.append(int(ranges))
            except:
                continue
    
    #drop duplicates
    page_list = list(dict.fromkeys(page_list))
    page_list.sort()
    return page_list
            
if __name__ == "__main__":
    lst = list_from_text(sys.argv[1])
    print(str(lst))