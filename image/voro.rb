
def z; 4; end
def w;
  800*z
end

def pos
  loop do
    r = rand*(w/1.4)
    t = rand*(Math::PI*2)
    x = r*Math.cos(t) + w/2
    y = r*Math.sin(t) + w/2
    return [x,y].join(",") if (0...w)===x && (0...w)===y
  end
end

cols = [*0...0xfff].shuffle.take(0x400).map{ |e| "#{pos},##{"%03x" % e}" }

cmd = [
  "-size #{w}x#{w}",
  "xc:  -colorspace RGB",
  "-sparse-color voronoi '#{cols.join(" ")}'",
  "-resize #{100.0/z}%",
  "-define png:bit-depth=8",
  "voro.png",
]

%x( magick #{cmd.join(" ")})