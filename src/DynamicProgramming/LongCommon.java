/*
 * Written by Joir-dan Gumbs
 * HANABI and SAKURASOUND are code names for Joir-dan Gumbs
 * 2011
 */

import static java.lang.System.out;

import java.util.Arrays;


public class LongCommon {
        public static void main(String... args) {
            LongCommon.lcs("ABCBDAB", "BDCABA");
        }

        
        public static void lcs(String x, String y){
            int m = x.length();
            int n = y.length();
             
            char[][] b= new char[m][n];
            int[][] c= new int[m][n];
            for(int i= 1;i < m; i++) c[i][0] = 0;
            for(int i= 0;i < n; i++) c[0][i] = 0;
            
            for(int i =1; i < m; i++){
                for(int j = 1; j < n; j++){
                    if(x.charAt(i) == y.charAt(j)){
                        c[i][j] = c[i-1][j-1] + 1;
                        b[i][j] = 0x2196;
                    }
                    else if(c[i -1][j] >= c[i][j-1]){
                        c[i][j] = c[i-1][j];
                        b[i][j] = '↑';
                    }
                    else{
                        c[i][j] = c[i][j-1];
                        b[i][j] = '←';
                    }
                }
            }
            out.printf("  %s\n", Arrays.toString(y.toCharArray()));
            for(int i = 0; i < m;i++){
                out.printf("%s ", x.charAt(i));
                out.println(Arrays.toString(b[i]));    
            } 
            out.printf("  %s\n", Arrays.toString(y.toCharArray()));
            for(int i = 0; i < m;i++){
                out.printf("%s ", x.charAt(i));
                out.println(Arrays.toString(c[i]));    
            }  
        }
        
        
    }
