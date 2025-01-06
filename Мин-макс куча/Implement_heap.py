# void siftup(vector<int>& a, int i){
#     while(i != 0 and a[(i - 1) / 2] > a[i]){
#         swap(a[i], a[(i - 1) / 2]);
#         i = (i - 1) / 2;
#     }
# }
#
# void siftdown(vector<int>& a, int i){
#     while(2 * i + 1 < a.size()){
#         int u = (2 * i + 1);
#         if (2 * i + 2 < a.size() and a[2 * i + 2] < a[u]){
#             u = 2 * i + 2;
#         }
#         if (a[u] < a[i]){
#             swap(a[u], a[i]);
#             i = u;
#         }
#         else{
#             break;
#         }
#     }
# }
