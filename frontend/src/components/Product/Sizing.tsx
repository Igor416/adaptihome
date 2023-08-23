import { Size } from "../../JSONTypes";
import SizeDisplay from "../_reusables/SizeDisplay";
import Circle from "./Circle";

interface SizingProps {
  sizes: Size[],
  pickedSize: number,
  pickSize: (val: number) => void,
  t: (val: string) => string
}

export default function Sizing({sizes, pickedSize, pickSize, t}: SizingProps) {
  const widths: number[] = []
  sizes.map(size => size.width).forEach(width => {
    if (!widths.includes(width)) {
      widths.push(width);
    }
  });
  const lengths: number[] = []
  sizes.map(size => size.length).forEach(length => {
    if (!lengths.includes(length)) {
      lengths.push(length);
    }
  });
  for (let i = 1; i < widths.length + 1; i++) {
    const ones = Array(lengths.length)
    widths.splice(i, 0, ...ones)
    i += lengths.length
  }

  const getSize = (width: number, length: number) => {
    const size = sizes.filter(size => size.width === width && size.length === length)
    if (size.length === 0) {
      return undefined
    }
    return size[0]
  }

  return <div className='d-flex justify-content-start align-items-center mx-5 px-5'>
    <div style={{gridTemplateColumns: 'auto '.repeat(lengths.length + 1)}} className='d-grid mx-5'>
      <div className='p-1 border-blue' />
      {lengths.sort().map((length, i) =>
        <div key={i} className='p-1 border-start border-blue h5'>{length}</div>
      )}
      {widths.map((width, i) => {
        if (width === undefined) {
          const size = getSize(widths[i - (i % (lengths.length + 1))], lengths[(i - 1) % (lengths.length + 1)])
          return <div key={i} className='d-flex justify-content-center p-1 border-start border-top border-blue h5'>
            {size && <Circle key={i} size={1.5} color='teal' active={sizes.indexOf(size) === pickedSize} setActive={() => pickSize(sizes.indexOf(size))} />}
          </div>
        }
        return <div key={i} className='p-1 border-top border-blue h5 text-end'>{width}</div>
      })}
    </div>
    <SizeDisplay size={sizes[pickedSize]} t={t} />
  </div>
}