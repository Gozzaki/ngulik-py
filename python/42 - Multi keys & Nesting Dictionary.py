import datetime

mahasiswa1 = {
    'nama' : 'gozali',
    'nim'  : '21416255201215' ,
    'sks_lulus' : 21,
    'beasiswa' : False,
    'lahir' : datetime.datetime(2003,6,17)

}
mahasiswa2 = {
    'nama' : 'bayu ipe',
    'nim'  : '21416255201117' ,
    'sks_lulus' : 21,
    'beasiswa' : False,
    'lahir' : datetime.datetime(2003,6,17)

}
mahasiswa3 = {
    'nama' : 'deni TX',
    'nim'  : '21416255201234' ,
    'sks_lulus' : 21,
    'beasiswa' : True,
    'lahir' : datetime.datetime(2003,6,17)

}
data_mahasiswa = {
    'MAH001': mahasiswa1,
    'MAH002': mahasiswa2,
    'MAH003': mahasiswa3
}

print(data_mahasiswa)
print(f"{'KEY':<6} {'nama':<17} {'SKS':<5} {'Beasiswa':<9} {'lahir':<10}")
print('-'*50)

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa

    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks_lulus']
    BEASISWA = str(data_mahasiswa[KEY]['beasiswa'])
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")
    print(f"{KEY:<6} {NAMA:<17} {SKS:<5} {BEASISWA:<9} {LAHIR:<10}")
