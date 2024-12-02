use std::fs::File;
use std::io::Read;

fn main() {
    println!("load file!");
}

fn load_data(file_path: &str) -> String {
    let mut file = File::open(file_path).unwrap();

    let mut contents = String::new();

    file.read_to_string(&mut contents)
        .expect("Something went wrong");

    contents
}

fn map(data: &str) -> Vec<Vec<i32>>{
    vec![
        vec![3, 4, 2, 1, 3, 3],
        vec![4, 3, 5, 3, 9, 3]
    ]
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_read_file() {
        let result = load_data("./src/test_input.txt");

        assert_eq!(result, "3   4\n4   3\n2   5\n1   3\n3   9\n3   3");
    }

    #[test]
    fn it_split_data() {

        let result = map("3   4\n4   3\n2   5\n1   3\n3   9\n3   3");
        assert_eq!(result[0], vec![3, 4, 2, 1, 3, 3]);
        assert_eq!(result[1], vec![4, 3, 5, 3, 9, 3]);
    }
}
