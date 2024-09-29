require "csv"

def test(fn) 
  CSV.open( "#{fn}.csv", "w") do |csv|
    csv << %w( q jpeg_diff jpeg_size webp_diff webp_size avif_diff avif_size )
    1.step(99,1).each do |q|
      r = [q]
      %w( .jpeg .webp ).each do |ext|
        dest = "./tmp/#{fn}#{ext}"
        %x(magick ../image/#{fn}.png -quality #{q} #{dest})
        r += [
          %x(../diff/imdiff ../image/#{fn}.png #{dest}).strip,
          File.size(dest)
        ]
      end

      dest0 = "./tmp/#{fn}.avif"
      dest1 = "./tmp/#{fn}.avif.png"
      %x(magick ../image/#{fn}.png -quality #{q} #{dest0})
      %x(magick #{dest0} #{dest1})
      r += [
        %x(../diff/imdiff ../image/#{fn}.png #{dest1}).strip,
        File.size(dest0)
      ]
      csv << r
    end
  end
end

%w(b).each do |fn|
  test(fn)
end  

