import requests



def get_token():
    # URL endpoint login
    url = "https://apisdev-gw.beacukai.go.id/nle-oauth/v1/user/login"

    # Data body untuk login
    data = {
        "username": "bsl.lokal01",
        "password": "Buana4sl!"
    }

    # Melakukan permintaan POST untuk login
    response = requests.post(url, json=data)

    # Mengecek status kode response
    if response.status_code == 200:
        # Berhasil login, Anda dapat mengakses token atau data lainnya dari response
        print(response.json())
        access_token = response.json()["item"]["access_token"]
        return access_token
    else:
        # Gagal login, menampilkan pesan kesalahan
        print("Gagal login. Kode status:", response.status_code)
        print("Pesan kesalahan:", response.text)
        return 0


def get_dokumen(npwp, token):
    # Query parameter idPerusahaan
    params = {'idPerusahaan': str(npwp)}

    # Melakukan permintaan GET dengan query parameter
    response = requests.get("https://apis-gw.beacukai.go.id/openapi/status", params=params, headers={'Authorization': 'Bearer ' + token})

    # Mengecek status kode response
    if response.status_code == 200:
        # Berhasil mendapatkan response, menampilkan data JSON
        data_perusahaan = response.json()
        print(data_perusahaan)
        return data_perusahaan
    else:
        # Gagal mendapatkan response, menampilkan pesan kesalahan
        print("Gagal mendapatkan data perusahaan. Kode status:", response.status_code)
        return None


def get_bc_1_4(nomor_aju, token):
    # Query parameter idPerusahaan
    params = {'noAju': str(nomor_aju)}

    # Melakukan permintaan GET dengan query parameter
    response = requests.get("https://apis-gw.beacukai.go.id/barkir-public-service/public-barkir", params=params, headers={'Authorization': 'Bearer ' + token})

    # Mengecek status kode response
    if response.status_code == 200:
        # Berhasil mendapatkan response, menampilkan data JSON
        data_perusahaan = response.json()
        print(data_perusahaan)
        return data_perusahaan
    else:
        # Gagal mendapatkan response, menampilkan pesan kesalahan
        print("Gagal mendapatkan data perusahaan. Kode status:", response.status_code)
        return None