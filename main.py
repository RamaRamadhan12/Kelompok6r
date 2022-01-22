# import library brython
from browser import document, alert 

# deklarasi Variabel
input = document['input1']
button = document['btn']
output = document['output']
selectType = document['select-type']
selectCalculated = document['select-calculated']

#Perhitungan konversi berat menggunakan lambda
type1 = {'Gram' : {'Gram' : {'Rumus': lambda berat: berat, 'input': 'Masukkan Nilai'},
                'Ons': {'Rumus': lambda berat: berat / 100, 'input': 'Masukkan Nilai'},
                'Kilogram': {'Rumus': lambda berat: berat / 1000, 'input': 'Masukkan Nilai'},
                'Kwintal': {'Rumus': lambda berat: berat / 100000, 'input': 'Masukkan Nilai'},
                'Ton': {'Rumus': lambda berat: berat / 1000000, 'input': 'Masukkan Nilai'}},
        'Ons': {'Ons': {'Rumus': lambda berat:berat, 'input': 'Masukkan Nilai'},
                'Gram': {'Rumus': lambda berat: berat * 100, 'input': 'Masukkan Nilai'},
                'Kilogram': {'Rumus': lambda berat: berat / 10, 'input': 'Masukkan Nilai'},
                'Kwintal': {'Rumus': lambda berat: berat / 1000, 'input': 'Masukkan Nilai'},
                'Ton': {'Rumus': lambda berat: berat / 10000, 'input': 'Masukkan Nilai'}},
        'Kilogram': {'Kilogram': {'Rumus': lambda berat:berat, 'input': 'Masukkan Nilai'},
                'Gram': {'Rumus': lambda berat: berat * 1000, 'input': 'Masukkan Nilai'},
                'Ons': {'Rumus': lambda berat: berat * 10, 'input': 'Masukkan Nilai'},
                'Kwintal': {'Rumus': lambda berat: berat / 100, 'input': 'Masukkan Nilai'},
                'Ton': {'Rumus': lambda berat: berat / 1000, 'input': 'Masukkan Nilai'}},
        'Kwintal': {'Kwintal': {'Rumus': lambda berat:berat, 'input': 'Masukkan Nilai'},
                'Gram': {'Rumus': lambda berat: berat * 100000, 'input': 'Masukkan Nilai'},
                'Ons': {'Rumus': lambda berat: berat * 1000, 'input': 'Masukkan Nilai'},
                'Kilogram': {'Rumus': lambda berat: berat * 100, 'input': 'Masukkan Nilai'},
                'Ton': {'Rumus': lambda berat: berat / 10, 'input': 'Masukkan Nilai'}},
        'Ton': {'Ton': {'Rumus': lambda berat:berat, 'input': 'Masukkan Nilai'},
                'Gram': {'Rumus': lambda berat: berat * 1000000, 'input': 'Masukkan Nilai'},
                'Ons': {'Rumus': lambda berat: berat * 10000, 'input': 'Masukkan Nilai'},
                'Kilogram': {'Rumus': lambda berat: berat * 1000, 'input': 'Masukkan Nilai'},
                'Ton': {'Rumus': lambda berat: berat * 10, 'input': 'Masukkan Nilai'}}}

# Akan dijalankan pada saat pilihan diubah dari satuan berat 
def selectTypeAction(ev):
    x = selectType.value
    # Reset Input Field
    for i in range(1, 5):
        input[str(i)].value = ''
        input[str(i)].disabled = False

# Fungsi untuk mengubah string dari input ke int atau float
def getNum(x):
    temp = x
    # Convert string ke int
    try:
        temp = int(x)
    # Jika convert string ke int gagal (ValueError), maka convert ke float
    except ValueError:
        temp = float(x)
    finally:
        # Jika input (var temp) masih string (gagal convert ke int dan float), 
        # maka munculkan alert dan return dengan variable kosong ('')
        if temp != '' and type(temp) is str:
            alert('Harap masukkan berat')
            temp = ''
            input.value = temp
            return temp
        # Jika salah satu convert berhasil, maka return
        else:
            return temp

# Fungsi untuk memanggil rumus pada dictionary
def Rumus(x, num1):
    y = selectCalculated.value
    for key in type1.keys():
        if key.find(x) > -1:
            return type1[x][y]['Rumus'](num1)

# Fungsi utama
# Ketika button di-click atau menekan tombol enter maka program akan jalan
def main(ev):
    num1 = getNum(input1.value)
    result = Rumus(selectType.value, num1)
    output.textContent = str(result)

# Fugnsi keyEnter
# Fungsi yang mengarahkan ke Fungsi Main ketika tombol enter ditekan
def keyEnter(ev):
    traceKey = f"{ev.code}"
    if traceKey == 'Enter':
        main(0)

selectType.bind('change', selectTypeAction) # Ketika pilihan berat berubah, maka akan menjalankan fungsinya
button.bind('click', main) # Fungsi Main akan dipanggil ketika button di-click

# ketika enter ditekan pada salah satu input field maka akan diarahkan ke Fungsi keyEnter 
input1.bind("keypress", keyEnter)
