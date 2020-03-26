class Solution {
    public int countComponents(int n, int[][] edges) {
        int count = 0;
        Map<Integer, List<Integer>> adj_list = new HashMap<>();
        Set<Integer> seen = new HashSet<>();
        for (int i = 0; i < n; i ++){
            adj_list.put(i, new ArrayList<Integer>());
        }
        for (int[] edge: edges){
            adj_list.get(edge[0]).add(edge[1]);
            adj_list.get(edge[1]).add(edge[0]);
        }
        for (int node = 0; node < n; node++ ){
            if (!seen.contains(node)){
                dfs(node, adj_list, seen);
                count++;
            }
        }
        return count;
    }
    
    private void dfs(int node, Map<Integer, List<Integer>> adj_list, Set<Integer> seen){
        Stack<Integer> stack = new Stack<Integer>();
        stack.push(node);
        seen.add(node);
        while (!stack.isEmpty()){
            int curr_node = stack.pop();
            for (int neighbor: adj_list.get(curr_node)){
                if (!seen.contains(neighbor)){
                    seen.add(neighbor);
                    stack.push(neighbor);
                }
            }
        }
        
    }
}
