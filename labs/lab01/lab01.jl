# ---------------------------------------------------------
# Common setup: Russian alphabet (lowercase), and index maps
# ---------------------------------------------------------
const RU_ALPHABET = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
const chars_length = length(RU_ALPHABET)  # 33

# Build char -> index (0-based) and index -> char maps
const char_to_index = Dict(c => i - 1 for (i, c) in enumerate(RU_ALPHABET))
const index_to_char = Dict(i - 1 => c for (i, c) in enumerate(RU_ALPHABET))

# ---------------------------------------------------------
# Caesar cipher with arbitrary key k
# T^k(a) = (a + k) mod chars_length
# ---------------------------------------------------------
function caesar_encrypt(text::String, k::Int)
    result = IOBuffer()
    for ch in text
        lower_ch = lowercase(ch)
        if haskey(char_to_index, lower_ch)
            idx = char_to_index[lower_ch]
            new_idx = mod(idx + k, chars_length)
            new_ch = index_to_char[new_idx]
            # preserve original case
            write(result, isuppercase(ch) ? uppercase(new_ch) : new_ch)
        else
            write(result, ch)  # leave spaces/punctuation untouched
        end
    end
    return String(take!(result))
end

function caesar_decrypt(text::String, k::Int)
    return caesar_encrypt(text, -k)  # decrypting is just shifting back
end

# ---------------------------------------------------------
# Atbash cipher: mirror mapping, T(a) = (chars_length - 1 - a)
# Self-inverse: same function encrypts and decrypts
# ---------------------------------------------------------
function atbash(text::String)
    result = IOBuffer()
    for ch in text
        lower_ch = lowercase(ch)
        if haskey(char_to_index, lower_ch)
            idx = char_to_index[lower_ch]
            new_idx = chars_length - 1 - idx
            new_ch = index_to_char[new_idx]
            write(result, isuppercase(ch) ? uppercase(new_ch) : new_ch)
        else
            write(result, ch)
        end
    end
    return String(take!(result))
end

# ---------------------------------------------------------
# Demo
# ---------------------------------------------------------
plaintext = "привет мир"

k = 3
ciphertext = caesar_encrypt(plaintext, k)
decrypted  = caesar_decrypt(ciphertext, k)

println("Original:        ", plaintext)
println("Caesar (k=$k):    ", ciphertext)
println("Decrypted back:   ", decrypted)

atbash_text = atbash(plaintext)
atbash_back = atbash(atbash_text)

println("\nAtbash:           ", atbash_text)
println("Atbash again:     ", atbash_back)