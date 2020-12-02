let rec report_repair lst = match lst with
    [] -> 0
   | e::l -> let rec report2 l = match l with
    [] -> 0
   | e1::l2 -> if e + e1 = 2020 then (e*e1)
               else report2 l2 in report2 l;; 
