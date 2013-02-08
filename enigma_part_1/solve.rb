pos1 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
pos2 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
pos3 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

4.times do |rl|
  4.times do |rm|
    4.times do |rr|
      if rl != rm and rl != rr and rm != rr
        ['B','C'].each do |reflector|
          pos1.each do |p1|
            pos2.each do |p2|
              pos3.each do |p3|
                result = %x[./enigma.x "#{rl}#{rm}#{rr}" "#{reflector}" "#{p1}#{p2}#{p3}" data/enigmaCipher1.txt]
              puts result
              end
            end
          end
        end
      end
    end
  end
end



# a small test that everything works as expected
rl, rm, rr = 3, 0, 2
rflt=['B','C']

rflt.each do |r| 
  result = %x[./enigma.x "#{rl}#{rm}#{rr}" "#{r}" WAG data/ciphertext.txt]
  puts result
  puts result.size
end
