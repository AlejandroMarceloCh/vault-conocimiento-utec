---
curso: SISCOMP
titulo: 08 - Semana 6/S6_7seg_FPGA
slides: 7
fuente: 08 - Semana 6/S6_7seg_FPGA.pdf
---

Top_7seg_utec
// top_7seg_utec.v
// Muestra "UTEC" en los 4 displays de la Basys3

module top_7seg_utec (
   input wire clk,    // reloj de 100 MHz en Basys3
   input wire rst_n,    // reset activo bajo (por ejemplo BTN_C invertido)
   output reg [6:0] seg, // segmentos CA..CG (activos en LOW)
   output reg [3:0] an // anodos AN0..AN3 (activos en LOW)
);

  // -------------------------------
  // ROM con los caracteres a mostrar: "U", "T", "E", "C"
  // -------------------------------
  reg [6:0] rom [0:3]; // bit0=a ... bit6=g, 1=encendido
  initial begin
      // U
      rom[0] = 7'b0111110;
      // T
      rom[1] = 7'b0001111;
      // E
      rom[2] = 7'b1001111;
      // C
      rom[3] = 7'b1001110;
  end

  // -------------------------------
  // Divisor de frecuencia para multiplexado (~1 kHz por dígito)
  // -------------------------------
  localparam integer REFRESH_HZ = 1000; // frecuencia total por dígito
  localparam integer CLK_FREQ_HZ = 100_000_000;
  localparam integer REFRESH_COUNT = CLK_FREQ_HZ / (REFRESH_HZ * 4);

  reg [31:0] refresh_cnt;
  reg [1:0] digit_sel; // 0..3

  always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        refresh_cnt <= 0;
        digit_sel <= 0;
    end else begin
        if (refresh_cnt >= REFRESH_COUNT-1) begin
            refresh_cnt <= 0;
            digit_sel <= digit_sel + 1;
        end else begin
            refresh_cnt <= refresh_cnt + 1;
        end
    end
  end
  // -------------------------------
  // Selección de patrón y anodo
  // -------------------------------
  reg [6:0] pattern;
  always @* begin
      case (digit_sel)
         2'd0: begin pattern = rom[0]; an = 4'b1110; end // AN0
         2'd1: begin pattern = rom[1]; an = 4'b1101; end // AN1
         2'd2: begin pattern = rom[2]; an = 4'b1011; end // AN2
         2'd3: begin pattern = rom[3]; an = 4'b0111; end // AN3
         default: begin pattern = 7'b0000000; an = 4'b1111; end
      endcase
  end

  // -------------------------------
  // Salida de segmentos (activos en bajo)
  // -------------------------------
  always @* begin
      seg = ~pattern;
  end

endmodule
Top_7seg_Constraints
set_property PACKAGE_PIN W4 [get_ports {an[0]}]
set_property PACKAGE_PIN V4 [get_ports {an[1]}]
set_property PACKAGE_PIN U4 [get_ports {an[2]}]
set_property PACKAGE_PIN U2 [get_ports {an[3]}]

set_property PACKAGE_PIN U16 [get_ports {seg[0]}] # CA
set_property PACKAGE_PIN E19 [get_ports {seg[1]}] # CB
set_property PACKAGE_PIN U19 [get_ports {seg[2]}] # CC
set_property PACKAGE_PIN V19 [get_ports {seg[3]}] # CD
set_property PACKAGE_PIN W18 [get_ports {seg[4]}] # CE
set_property PACKAGE_PIN U15 [get_ports {seg[5]}] # CF
set_property PACKAGE_PIN U14 [get_ports {seg[6]}] # CG
Top_7seg_utec_tb
`timescale 1ns/1ps

module tb_top_7seg_utec;

  // Señales para DUT
  reg clk;
  reg rst_n;
  wire [6:0] seg;
  wire [3:0] an;

  // Instancia del DUT
  top_7seg_utec dut (
      .clk(clk),
      .rst_n(rst_n),
      .seg(seg),
      .an(an)
  );

  // Generador de reloj 100 MHz (periodo = 10 ns)
  initial begin
     clk = 0;
     forever #5 clk = ~clk; // toggle cada 5 ns
  end

  // Secuencia de reset
  initial begin
     rst_n = 0;
     #100;      // mantener reset bajo 100 ns
     rst_n = 1; // liberar reset
  end

  // Tiempo de simulación
  initial begin
     // Simular 10 ms de tiempo real
     // (100 MHz → 1 ciclo = 10 ns → 10 ms = 1e7 ns)
     #10_000_000;
     $stop;
  end

endmodule
