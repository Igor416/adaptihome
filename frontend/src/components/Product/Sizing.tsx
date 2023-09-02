import { ResponsiveProps } from '../..';
import { Size } from '../../JSONTypes';
import { TranslationProps } from '../../i18n';
import SizeDisplay from '../_reusables/SizeDisplay';
import Circle from './Circle';

interface SizingProps extends TranslationProps, ResponsiveProps {
  sizes: Size[],
  pickedSize: number,
  pickSize: (val: number) => void
}

export default function Sizing({sizes, pickedSize, pickSize, t, isMobile}: SizingProps) {
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

  return <div className='d-flex w-100 flex-column flex-sm-row justify-content-start align-items-center mx-sm-5 px-sm-5 p-4 py-sm-0'>
    <div style={{gridTemplateColumns: 'auto '.repeat(lengths.length + 1)}} className='w-100 d-grid mx-sm-5 mb-4 mb-sm-0'>
      <div className='p-1 border-blue' />
      {lengths.sort().map((length, i) =>
        <div key={i} className='p-1 border-start border-blue h5'>{length}</div>
      )}
      {widths.map((width, i) => {
        if (width === undefined) {
          const size = getSize(widths[i - (i % (lengths.length + 1))], lengths[(i - 1) % (lengths.length + 1)])
          return <div key={i} className='d-flex justify-content-center p-1 border-start border-top border-blue h5'>
            {size && <Circle key={i} size={isMobile ? 6 : 1.5} color='teal' active={sizes.indexOf(size) === pickedSize} setActive={() => pickSize(sizes.indexOf(size))} />}
          </div>
        }
        return <div key={i} className='p-1 border-top border-blue h5 text-end'>{width}</div>
      })}
    </div>
    <SizeDisplay size={sizes[pickedSize]} t={t} />
  </div>
}