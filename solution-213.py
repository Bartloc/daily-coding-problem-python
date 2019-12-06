def find_ip_num(ip_str,split_points=3,ip_cand='',ip_out=None):
    if ip_out is None:
        ip_out=[]
    if split_points<0:
        if not ip_str:            
            ip_out.append(ip_cand[:-1])
        return
    for j in range(1,4):
        if ip_str:
            part_ip=int(ip_str[:j])
            if part_ip<10 and j==1 or\
               100>part_ip>=10 and j==2 or\
               256>part_ip>=100 and j==3:
                find_ip_num(ip_str[j:],split_points-1,ip_cand+ip_str[:j] +'.',ip_out)
    return ip_out

assert find_ip_num('2542540123')==['254.25.40.123', '254.254.0.123']
assert find_ip_num('11111123')==['1.1.111.123','1.11.11.123','1.11.111.23','1.111.1.123','1.111.11.23',
                                 '1.111.112.3','11.1.11.123','11.1.111.23','11.11.1.123','11.11.11.23',
                                 '11.11.112.3','11.111.1.23','11.111.12.3','111.1.1.123','111.1.11.23',
                                 '111.1.112.3','111.11.1.23','111.11.12.3','111.111.2.3']
