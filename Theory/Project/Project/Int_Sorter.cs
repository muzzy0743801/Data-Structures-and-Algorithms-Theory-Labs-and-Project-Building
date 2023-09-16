using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Project
{
    class Int_Sorter
    {
        public Int_Sorter(string type, int[] array)
        {
            if (type == "bucket sort")
            {
                BucketSort(array);
            }
            else if(type == "bubble sort")
            {
                BubbleSort(array);
            }
            else if (type == "merge sort")
            {
                MergeSort(array, 0, array.Length - 1);
            }
            else if (type == "insertion sort")
            {
                InsertionSort(array);
            }
            else if (type == "selection sort")
            {
                SelectionSort(array);
            }
        }

        static public int[] BucketSort(int[] array)
        {
            List<int> buckets = new List<int>();
            for (int i = 0; i < array.Length; i++)
            {
                buckets.Add(array[i]);
            }
            buckets.Sort();
            for (int i = 0; i < array.Length; i++)
            {
                array[i] = buckets[i];
            }
            foreach (var item in array)
                Console.Write(item + " ");
            Console.WriteLine();
            return array;
        }

        static public int[] BubbleSort(int[] array)
        {
            for (int p = 0; p < array.Length - 1; p++)
            {
                bool checker = true;
                for (int i = 0; i < array.Length - p - 1; i++)
                {
                    if (array[i] > array[i + 1])
                    {
                        int temp = array[i + 1];
                        array[i + 1] = array[i];
                        array[i] = temp;
                        checker = false;
                    }
                }
                if (checker == true)
                {
                    break;
                }
            }
            return array;
        }

        public static int[] MergeSort(int[] array, int start, int end)
        {
            if (start < end)
            {
                int mid = start + (end - start) / 2;
                MergeSort(array, start, mid);
                MergeSort(array, mid + 1, end);
                MergerSort(array, start, mid, end);
            }
            return array;
        }
        public static void MergerSort(int[] array, int start, int mid, int end)
        {
            int n1 = mid - start + 1;
            int n2 = end - mid;
            int[] L = new int[n1];
            int[] R = new int[n2];
            int i, j;
            for (i = 0; i < n1; ++i)
                L[i] = array[start + i];
            for (j = 0; j < n2; ++j)
                R[j] = array[mid + 1 + j];
            j = 0;
            int k = start;
            for (i = 0; i < n1 && j < n2; k++)
            {
                if (L[i] <= R[j])
                {
                    array[k] = L[i];
                    i++;
                }
                else
                {
                    array[k] = R[j];
                    j++;
                }
            }
            for (; i < n1; i++)
            {
                array[k] = L[i];
                k++;
            }
            for (; j < n2; j++)
            {
                array[k] = R[j];
                k++;
            }
        }
        static public int[] InsertionSort(int[] array)
        {
            for (int i = 0; i < array.Length - 1; i++)
            {
                if (array[i] > array[i + 1])
                {
                    for (int j = i + 1; j > 0; j--)
                    {
                        if (array[j - 1] > array[j])
                        {
                            int temp = array[j - 1];
                            array[j - 1] = array[j];
                            array[j] = temp;
                        }
                        else
                            break;
                    }
                }
            }
            return array;
        }

        public static int[] SelectionSort(int[] array)
        {
            for (int i = 0; i < array.Length - 1; i++)
            {
                int minimum = i;
                for (int j = i + 1; j < array.Length; j++)
                    if (array[j] < array[minimum])
                        minimum = j;
                int temp = array[minimum];
                array[minimum] = array[i];
                array[i] = temp;
            }
            return array;
        }
    }
}
