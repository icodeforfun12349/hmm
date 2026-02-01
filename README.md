a free captcha solver i made, have fun. it uses 10 methods.
1. **Standard**: 3x upscale, 2.5x contrast, sharpness, threshold 140, median filtera
2. **High Contrast**: 4x upscale, 3.5x contrast, threshold 130
3. **Low Threshold**: 3x upscale, 2.0x contrast, threshold 110
4. **High Threshold**: 3x upscale, 2.5x contrast, threshold 170
5. **Inverted Colors**: Invert → 3x upscale → 2.5x contrast → threshold 140
6. **Heavy Denoising**: 3x upscale → median filter 5 → 3.0x contrast
7. **Edge Enhancement**: 3x upscale → edge enhance → 2.5x contrast
8. **Super Sharp**: 4x upscale → 3.0x sharpness → 2.5x contrast
9. **Minimal Processing**: 2x upscale → 1.5x contrast (less is more!)
10. **Bilateral Filter**: 3x upscale → smooth → 2.8x contrast → threshold 150
