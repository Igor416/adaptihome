import { Size } from "../../JSONTypes"
import { TranslationProps } from "../../i18n"

interface SizeDisplayProps extends TranslationProps {
  size: Size
}

export default function SizeDisplay({size, t}: SizeDisplayProps) {
  return <div className='d-flex flex-column ms-4 h6'>
    <div>
      <span>{t('length')}</span>
      <span className='mx-1'>x</span>
      <span>{t('width')}:</span>
    </div>
    <div className='text-blue h5'>
      <span>{size.length} cm</span>
      <span className='mx-1'>x</span>
      <span>{size.width} cm</span>
    </div>
  </div>
}