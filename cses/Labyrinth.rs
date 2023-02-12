use std::io;
use std::collections::VecDeque;

macro_rules! parse_line {
    ($($t: ty),+) => ({
        let mut a_str = String::new();
        io::stdin().read_line(&mut a_str).expect("read error");
        let mut a_iter = a_str.split_whitespace();
        (
            $(
            a_iter.next().unwrap().parse::<$t>().expect("parse error"),
            )+
        )
    })
}

const DIMES: [(i32, i32); 4] = [(-1,0), (1,0), (0,1), (0,-1)];
const DIMES_STR: [char; 4] = ['U', 'D', 'R', 'L'];

fn main() {
    let (n, m) = parse_line!(i32,i32);
    let (mut si, mut sj, mut ei, mut ej) = (-1, -1, -1, -1);
    let mut map = vec![vec!['N'; m as usize]; n as usize];
    let mut dir = vec![vec![5; m as usize]; n as usize];
    let mut deque: VecDeque<(i32, i32)> = VecDeque::new();
    for i in 0..n {
        let mut instr = String::new();
        io::stdin().read_line(&mut instr).expect("read error");
        let chars: Vec<char> = instr.chars().collect();
        for j in 0..m {
            map[i as usize][j as usize] = chars[j as usize];
            if map[i as usize][j as usize] == 'A' {
                si = i;
                sj = j;
            } else if map[i as usize][j as usize] == 'B' {
                ei = i;
                ej = j;
            } 
        }
    }
    deque.push_back((si, sj));
    map[si as usize][sj as usize] = '#';

    'main_while: while !deque.is_empty() {
        let (curi, curj) = if let Some((curi, curj)) = deque.pop_front() { (curi, curj) } else { todo!() };
        for i in 0..4 {
            let ci = curi + DIMES[i].0;
            let cj = curj + DIMES[i].1;
            if ci == ei && cj == ej {
                map[ci as usize][cj as usize] = '#';
                dir[ci as usize][cj as usize] = i;
                break 'main_while
            }
            if ci >= n || ci < 0 || cj >= m || cj < 0 || map[ci as usize][cj as usize] == '#' {
                continue;
            }
            map[ci as usize][cj as usize] = '#';
            dir[ci as usize][cj as usize] = i;
            deque.push_back((ci, cj));
        }
    }

    if map[ei as usize][ej as usize] == '#' {
        println!("YES");
        let mut ci = ei;
        let mut cj = ej;
        let mut res_vec: VecDeque<char> = VecDeque::new();
        while ci != si || cj != sj {
            let direction = dir[ci as usize][cj as usize];
            res_vec.push_front(DIMES_STR[direction as usize]);
            ci -= DIMES[direction as usize].0;
            cj -= DIMES[direction as usize].1;
        }
        let res: String = res_vec.iter().collect();
        println!("{}", res.len());
        println!("{}", res);
    } else {
        println!("NO");
    }
}