# WinEncrypt

WinEncrypt is a simple Python program that provides file encryption and decryption services for data security on Windows. It uses the `cryptography` library to perform encryption and decryption, ensuring your files remain secure.

## Features

- **Encryption**: Encrypt any file to protect its contents.
- **Decryption**: Decrypt previously encrypted files to access their original contents.
- **Key Management**: Automatically generates and manages an encryption key.

## Requirements

- Python 3.x
- `cryptography` library

To install the required `cryptography` library, use the following command:

```bash
pip install cryptography
```

## Usage

Run the program through command line with the following syntax:

```bash
python WinEncrypt.py <action> <file> [--key-file <key-file>]
```

- `<action>`: Specify the action to perform - `encrypt` or `decrypt`.
- `<file>`: Path to the file you want to encrypt or decrypt.
- `--key-file <key-file>` (optional): Path to the encryption key file. Defaults to `secret.key`.

### Examples

To encrypt a file named `myfile.txt`:

```bash
python WinEncrypt.py encrypt myfile.txt
```

To decrypt a file named `myfile.txt`:

```bash
python WinEncrypt.py decrypt myfile.txt
```

### Important

- Ensure you keep the encryption key file (`secret.key` by default) secure. Losing the key will make it impossible to decrypt your files.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.