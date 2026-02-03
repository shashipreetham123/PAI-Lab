function solution(m, n, d) {
    
    if(d > Math.max(m, n)) return -1;
    
    let q = [];
    let visited = [];
    for(let i = 0; i <= m + 1; i++) {
        visited.push([])
        let arr = [];
        for(let j = 0; j <= n + 1; j++) {
            arr.push(false)
        }    
        visited.push(arr);
    }
    q.push([0, 0, [[0, 0, "Initial State"]]]);
    visited[0][0] = true;
    
    while(q.length != 0) {
        const curr = q.shift();
        const jug1 = curr[0];
        const jug2 = curr[1];
        const path = curr[2]
       
        
        if (jug1 == d) {
            if(jug2 != 0) {
                path.push([d, 0, "Empty jug 2"]);
            }
            return path
        };
        if (jug2 == d) {
            if(jug1 != 0) {
                path.push([0, d, "Empty jug 1"]);
            }
            return path
        };
        
        // 1. Fill Jug 1
        if(!visited[m][jug2] && jug1 < m) {
            const steps = [...curr[2]];
            visited[m][jug2] = true;
            steps.push([m, jug2, "Fill Jug 1"])
            q.push([m, jug2, steps]);
        }
        // 2. Fill Jug 2
        if(!visited[jug1][n] && jug2 < n) {
            const steps = [...curr[2]];
            visited[jug1][n] = true;
            steps.push([jug1, n, "Fill Jug 2"])
            q.push([jug1, n, steps]);
        }
        // // 3. Pour some water out of the jug 1
        // if(jug1 > 0) {
        //     for(let i = 1; i <= jug1; i++) {
        //         if(!visited[jug1 - i][jug2]) {
        //             const steps = [...curr[2]];
        //             visited[jug1 - i][jug2] = true;
        //             steps.push([jug1 - i, jug2, `Pour ${i} litres water out of the jug 1`])
        //             q.push([jug1 - i, jug2, steps]);
        //         }
        //     }
        // }
        // // 4. Pour some water out of the jug 2
        // if(jug2 > 0) {
        //     for(let i = 1; i <= jug2; i++) {
        //         if(!visited[jug1][jug2 - i]) {
        //             const steps = [...curr[2]];
        //             visited[jug1][jug2 - i] = true;
        //             steps.push([jug1, jug2 - i, `Pour ${i} litres water out of the jug 2`])
        //             q.push([jug1, jug2 - i, steps]);
        //         }
        //     }
        // }
        // 5. Empty jug1
        if (!visited[0][jug2]) {
            visited[0][jug2] = true;
            const steps = [...curr[2]];
            steps.push([0, jug2, "Empty jug1"])
            q.push([0, jug2, steps]);
        }

        // 6. Empty jug2
        if (!visited[jug1][0]) {
            visited[jug1][0] = true;
            const steps = [...curr[2]];
            steps.push([jug1, 0, "Empty jug2"])
            q.push([jug1, 0, steps]);
        }
        
        // 7. Pour Water from jug2 to jug 1
        if(jug1 + jug2 >= m && jug2 > 0) {
            if (!visited[m][jug2 - (m - jug1)]) {
                visited[m][jug2 - (m - jug1)] = true;
                const steps = [...curr[2]];
                steps.push([m, jug2 - (m - jug1), "Pour Water from jug2 to jug 1 until jug1 is full"])
                q.push([m, jug2 - (m - jug1), steps]);
            }
        }
        
        // 8. Pour Water from jug1 to jug 2
        if(jug1 + jug2 >= n && jug1 > 0) {
            if (!visited[jug1 - (n - jug2)][n]) {
                visited[jug1 - (n - jug2)][n] = true;
                const steps = [...curr[2]];
                steps.push([jug1 - (n - jug2), n, "Pour Water from jug1 to jug 2 until jug 2 is full"])
                q.push([jug1 - (n - jug2), n, steps]);
            }
        }
        
        // 9. Pour all water from jug2 to jug 1
        if(jug1 + jug2 <= m && jug2 > 0) {
            if (!visited[jug1 + jug2][0]) {
                visited[jug1 + jug2][0] = true;
                const steps = [...curr[2]];
                steps.push([jug1 + jug2, 0, "Pour all water from jug2 to jug 1"])
                q.push([jug1 + jug2, 0, steps]);
            }
        }
        
        // 10. Pour all the water from jug1 to jug 2
        if(jug1 + jug2 <= n && jug1 > 0) {
            if (!visited[0][jug1 + jug2]) {
                visited[0][jug1 + jug2] = true;
                const steps = [...curr[2]];
                steps.push([0, jug1 + jug2, "Pour all the water from jug1 to jug 2"])
                q.push([0, jug1 + jug2, steps]);
            }
        }
        
    }
    return -1;
    
}

function main() {
    let a = parseInt(prompt("Enter Capacity of Jug 1 : "));
    let b = parseInt(prompt("Enter Capacity of Jug 2 : "));
    let d = parseInt(prompt("Enter the Target : "));
    
    let sol = solution(a, b, d);
    
    if(sol != -1) {
        console.log(sol);
    }else{
        console.log("No Solution.")
    }
}


main()
