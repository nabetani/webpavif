require "csv"

def test(fn, prfix, range) 
  CSV.open( [prfix,fn].compact.join("_")+".csv", "w") do |csv|
    csv << %w( q jpeg_diff jpeg_size webp_diff webp_size jp2_diff jp2_size avif_diff avif_size )
    png = "../image/#{fn}.png"
    pngSize = File.size(png).to_f
    range.each do |q|
      print "."
      r = [q]
      %w( .jpeg .webp .jp2 ).each do |ext|
        dest = "./tmp/#{fn}#{ext}"
        %x(magick #{png} -quality #{q} #{dest})
        r += [
          %x(../diff/imdiff #{png} #{dest}).strip,
          File.size(dest) / pngSize
        ]
      end

      dest0 = "./tmp/#{fn}.avif"
      dest1 = "./tmp/#{fn}.avif.png"
      %x(magick #{png} -quality #{q} #{dest0})
      %x(magick #{dest0} #{dest1})
      r += [
        %x(../diff/imdiff ../image/#{fn}.png #{dest1}).strip,
        File.size(dest0) / pngSize
      ]
      csv << r
    end
  end
  puts
end

IMAGES = %w(jfish ham cloud turtle dog voro)

def loq
  IMAGES.each do |fn|
    p fn
    test(fn, nil, (1..99))
  end  
end

def hiq
  IMAGES.each do |fn|
    p fn
    test(fn, "hiq", (99..100))
  end  
end

loq
hiq

