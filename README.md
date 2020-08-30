# Merge sort Algorithm

Merge Sort is a Divide and Conquer algorithm. It divides input array in two halves, calls itself for the two halves and then merges the two sorted halves.


## Working of this algorithm:
- The array/list is recursively divided in two halves till the size becomes 1
- Once the size becomes 1, the merge processes comes into action and starts merging arrays back till the complete array is merged.
- It repeats until no input elements remain.


## Complexity:
- Merge sort has an best, average and worst-case running time of O(n log(n)) which is way better than the O(n²) running time of most of the other sorting algorithms


## Advantages of Merge sort:

- It is excellent for sorting data that are normally accessed sequentially. e.g. linked lists, tape drive, hard disk
- It is quicker for larger lists because unlike insertion and bubble sort it doesnt go through the whole list seveal times.
- It has a consistent running time, carries out different bits with similar times in a stage.
- Can be coded to work in place but normally it's not inplace

## Disadvantages of Merge sort:

- Slower comparative to the other sort algorithms for smaller tasks.
- Uses more memory space to store the sub elements of the initial split list.


![ImgName](https://github.com/KarimsHub/Merge_sort_Algorithm/blob/master/merge_sort_image.png?raw=true)
